import zipfile
import xml.etree.ElementTree as ET

def check_for_canary_tokens(file_path):
    suspicious_indicators = []
    
    # Standard OpenXML namespaces used by Microsoft Word
    namespaces = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
        'rel': 'http://schemas.openxmlformats.org/package/2006/relationships'
    }

    try:
        with zipfile.ZipFile(file_path, 'r') as docx_zip:
            file_list = docx_zip.namelist()

            # ---------------------------------------------------------
            # 1. Scan ALL .rels files (document, headers, footers, etc.)
            # ---------------------------------------------------------
            for file_name in file_list:
                if file_name.endswith('.rels'):
                    try:
                        content = docx_zip.read(file_name).decode('utf-8', errors='ignore')
                        root = ET.fromstring(content)
                        
                        for rel in root.findall('rel:Relationship', namespaces):
                            target_mode = rel.attrib.get('TargetMode', '')
                            target = rel.attrib.get('Target', '')
                            
                            # Filter out internal files and Microsoft OpenXML schemas
                            if target_mode == 'External' or (
                                target.startswith(('http://', 'https://')) 
                                and 'schemas.openxmlformats.org' not in target
                                and 'schemas.microsoft.com' not in target
                            ):
                                suspicious_indicators.append({
                                    'file': file_name,
                                    'type': 'External Relationship (Web Bug / Token)',
                                    'target': target
                                })
                    except ET.ParseError:
                        pass

            # ---------------------------------------------------------
            # 2. Check for Attached Templates in word/settings.xml
            # ---------------------------------------------------------
            if 'word/settings.xml' in file_list:
                try:
                    settings_content = docx_zip.read('word/settings.xml')
                    settings_root = ET.fromstring(settings_content)
                    
                    attached_template = settings_root.find('.//w:attachedTemplate', namespaces)
                    
                    if attached_template is not None:
                        rel_id = (
                            attached_template.attrib.get(f"{{{namespaces['r']}}}id") 
                            or attached_template.attrib.get('r:id')
                        )
                        target_url = None
                        
                        # Resolve the relationship ID in settings.xml.rels
                        if rel_id and 'word/_rels/settings.xml.rels' in file_list:
                            rels_content = docx_zip.read('word/_rels/settings.xml.rels')
                            rels_root = ET.fromstring(rels_content)
                            for rel in rels_root.findall('rel:Relationship', namespaces):
                                if rel.attrib.get('Id') == rel_id:
                                    target_url = rel.attrib.get('Target')
                                    break
                        
                        suspicious_indicators.append({
                            'file': 'word/settings.xml',
                            'type': 'Potential Attached Template / Remote Setting',
                            'target': target_url if target_url else (f"Rel ID: {rel_id}" if rel_id else "Unresolved Attached Template")
                        })
                except ET.ParseError:
                    pass

            # ---------------------------------------------------------
            # 3. Check for embedded HTTP fields in word/document.xml
            # ---------------------------------------------------------
            if 'word/document.xml' in file_list:
                try:
                    doc_content = docx_zip.read('word/document.xml').decode('utf-8', errors='ignore')
                    if 'INCLUDEPICTURE' in doc_content or 'HYPERLINK' in doc_content:
                        doc_root = ET.fromstring(doc_content)
                        for elem in doc_root.iter():
                            text = elem.text or ''
                            if (
                                ('http://' in text or 'https://' in text) 
                                and 'schemas.openxmlformats.org' not in text
                                and 'schemas.microsoft.com' not in text
                            ):
                                suspicious_indicators.append({
                                    'file': 'word/document.xml',
                                    'type': 'Remote Link in Document Body',
                                    'target': text.strip()
                                })
                except ET.ParseError:
                    pass

    except (zipfile.BadZipFile, FileNotFoundError) as e:
        print(f"[!] Error reading file: {e}")
        return None

    return suspicious_indicators


# --- Main Execution ---
file_to_check = ""
results = check_for_canary_tokens(file_to_check)

if results is not None:
    if results:
        print(f"[!] Warning: Found {len(results)} potential Canary Token indicator(s):\n")
        for item in results:
            print(f"  - Location: {item['file']}")
            print(f"    Type:     {item['type']}")
            print(f"    Target:   {item['target']}\n")
        
        print("[!] VERDICT: File is NOT SAFE! Opening it in Word will trigger a remote alert.")
    else:
        print("[+] VERDICT: File is SAFE. No external network tokens or attached templates detected.")