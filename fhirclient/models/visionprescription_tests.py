#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import visionprescription
from fhirdate import FHIRDate


class VisionPrescriptionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = visionprescription.VisionPrescription(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testVisionPrescription1(self):
        inst = self.instantiate_from("visionprescription-example-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e3aab10> instance")
    
        self.assertEqual(inst.dateWritten.date, FHIRDate("2014-06-15").date)
        self.assertEqual(inst.dateWritten.isostring, "2014-06-15")
        self.assertEqual(inst.dispense[0].add, 1.75)
        self.assertEqual(inst.dispense[0].axis, 160)
        self.assertEqual(inst.dispense[0].backCurve, 8.7)
        self.assertEqual(inst.dispense[0].brand, "OphthaGuard")
        self.assertEqual(inst.dispense[0].color, "green")
        self.assertEqual(inst.dispense[0].cylinder, -2.25)
        self.assertEqual(inst.dispense[0].diameter, 14.0)
        self.assertEqual(inst.dispense[0].duration.code, "month")
        self.assertEqual(inst.dispense[0].duration.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dispense[0].duration.units, "month")
        self.assertEqual(inst.dispense[0].duration.value, 1)
        self.assertEqual(inst.dispense[0].eye, "right")
        self.assertEqual(inst.dispense[0].power, -2.75)
        self.assertEqual(inst.dispense[0].product.code, "contact")
        self.assertEqual(inst.dispense[0].product.system, "http://hl7.org/fhir/ex-visionprescriptionproduct")
        self.assertEqual(inst.dispense[1].add, 1.75)
        self.assertEqual(inst.dispense[1].axis, 160)
        self.assertEqual(inst.dispense[1].backCurve, 8.7)
        self.assertEqual(inst.dispense[1].brand, "OphthaGuard")
        self.assertEqual(inst.dispense[1].color, "green")
        self.assertEqual(inst.dispense[1].cylinder, -3.5)
        self.assertEqual(inst.dispense[1].diameter, 14.0)
        self.assertEqual(inst.dispense[1].duration.code, "month")
        self.assertEqual(inst.dispense[1].duration.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dispense[1].duration.units, "month")
        self.assertEqual(inst.dispense[1].duration.value, 1)
        self.assertEqual(inst.dispense[1].eye, "left")
        self.assertEqual(inst.dispense[1].power, -2.75)
        self.assertEqual(inst.dispense[1].product.code, "contact")
        self.assertEqual(inst.dispense[1].product.system, "http://hl7.org/fhir/ex-visionprescriptionproduct")
        self.assertEqual(inst.id, "33124")
        self.assertEqual(inst.identifier[0].system, "http://www.happysight.com/prescription")
        self.assertEqual(inst.identifier[0].value, "15014")
        self.assertEqual(inst.text.div, "<div>Sample Contract Lens prescription</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testVisionPrescription2(self):
        inst = self.instantiate_from("visionprescription-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e3aab10> instance")
    
        self.assertEqual(inst.dateWritten.date, FHIRDate("2014-06-15").date)
        self.assertEqual(inst.dateWritten.isostring, "2014-06-15")
        self.assertEqual(inst.dispense[0].add, 2.0)
        self.assertEqual(inst.dispense[0].base, "down")
        self.assertEqual(inst.dispense[0].eye, "right")
        self.assertEqual(inst.dispense[0].prism, 0.5)
        self.assertEqual(inst.dispense[0].product.code, "lens")
        self.assertEqual(inst.dispense[0].product.system, "http://hl7.org/fhir/ex-visionprescriptionproduct")
        self.assertEqual(inst.dispense[0].sphere, -2.0)
        self.assertEqual(inst.dispense[1].add, 2.0)
        self.assertEqual(inst.dispense[1].axis, 180)
        self.assertEqual(inst.dispense[1].base, "up")
        self.assertEqual(inst.dispense[1].cylinder, -0.5)
        self.assertEqual(inst.dispense[1].eye, "left")
        self.assertEqual(inst.dispense[1].prism, 0.5)
        self.assertEqual(inst.dispense[1].product.code, "lens")
        self.assertEqual(inst.dispense[1].product.system, "http://hl7.org/fhir/ex-visionprescriptionproduct")
        self.assertEqual(inst.dispense[1].sphere, -1.0)
        self.assertEqual(inst.id, "33123")
        self.assertEqual(inst.identifier[0].system, "http://www.happysight.com/prescription")
        self.assertEqual(inst.identifier[0].value, "15013")
        self.assertEqual(inst.text.div, "<div>\n	  \n      <p>OD -2.00 SPH         +2.00 add    0.5 p.d. BD</p>\n      \n      <p>OS -1.00 -0.50 x 180 +2.00 add    0.5 p.d. BU</p>\n    \n    </div>")
        self.assertEqual(inst.text.status, "generated")

