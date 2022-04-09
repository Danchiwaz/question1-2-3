# i will use a list to demonstrate the implementaton of xml 
import xml.etree.ElementTree as ET

EMPLOYEE_LIST = ['Samson Maina', 'Daniel Wachira Maina','Purity Wanjiku','Mary Odhiambo','Dennis Waweru']

def generate_xml():
    empl_config = ET.Element("empl_config")
    empl_config = ET.SubElement(empl_config, 'empl_config')

    for employee in range(len(EMPLOYEE_LIST)):
        emp = ET.SubElement(empl_config,"emp")
        emp.text = str(EMPLOYEE_LIST[employee])

    tree = ET.ElementTree(empl_config)
    tree.write("employee.xml", encoding="utf-8", xml_declaration=True)

generate_xml()

