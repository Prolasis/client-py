#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import device
from fhirdate import FHIRDate


class DeviceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = device.Device(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testDevice1(self):
        inst = self.instantiate_from("device-example-f001-feedingtube.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2c64d0> instance")
    
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.status, "available")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "25062003")
        self.assertEqual(inst.type.coding[0].display, "Feeding tube, device")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testDevice2(self):
        inst = self.instantiate_from("device-example-ihe-pcd.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2c64d0> instance")
    
        self.assertEqual(inst.id, "ihe-pcd")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "SNO")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://hl7.org/fhir/v2/0203")
        self.assertEqual(inst.identifier[0].type.text, "Serial Number")
        self.assertEqual(inst.identifier[0].value, "AMID-123-456")
        self.assertEqual(inst.lotNumber, "12345")
        self.assertEqual(inst.manufacturer, "Acme Devices, Inc")
        self.assertEqual(inst.model, "A.1.1")
        self.assertEqual(inst.text.div, "<div>\n      \n      <p>Acme Patient Monitor</p>\n    \n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.text, "Vital Signs Monitor")
    
    def testDevice3(self):
        inst = self.instantiate_from("device-example-pacemaker.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2c64d0> instance")
    
        self.assertEqual(inst.contact[0].system, "phone")
        self.assertEqual(inst.contact[0].value, "ext 4352")
        self.assertEqual(inst.id, "example-pacemaker")
        self.assertEqual(inst.identifier[0].system, "http://acme.com/devices/pacemakers/octane/serial")
        self.assertEqual(inst.identifier[0].value, "1234-5678-90AB-CDEF")
        self.assertEqual(inst.lotNumber, "1234-5678")
        self.assertEqual(inst.manufacturer, "Acme Devices, Inc")
        self.assertEqual(inst.model, "PM/Octane 2014")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "octane2014")
        self.assertEqual(inst.type.coding[0].display, "Performance pace maker for high octane patients")
        self.assertEqual(inst.type.coding[0].system, "http://acme.com/devices")
    
    def testDevice4(self):
        inst = self.instantiate_from("device-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2c64d0> instance")
    
        self.assertEqual(inst.contact[0].system, "phone")
        self.assertEqual(inst.contact[0].value, "ext 4352")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://goodcare.org/devices/id")
        self.assertEqual(inst.identifier[0].value, "345675")
        self.assertEqual(inst.identifier[1].type.coding[0].code, "SNO")
        self.assertEqual(inst.identifier[1].type.coding[0].system, "http://hl7.org/fhir/v2/0203")
        self.assertEqual(inst.identifier[1].type.text, "Serial Number")
        self.assertEqual(inst.identifier[1].value, "AMID-342135-8464")
        self.assertEqual(inst.lotNumber, "43453424")
        self.assertEqual(inst.manufacturer, "Acme Devices, Inc")
        self.assertEqual(inst.model, "AB 45-J")
        self.assertEqual(inst.status, "available")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "86184003")
        self.assertEqual(inst.type.coding[0].display, "Electrocardiographic monitor and recorder")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type.text, "ECG")

