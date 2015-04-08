#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import contraindication
from fhirdate import FHIRDate


class ContraindicationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = contraindication.Contraindication(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testContraindication1(self):
        inst = self.instantiate_from("contraindication-example-allergy.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2be110> instance")
    
        self.assertEqual(inst.id, "allergy")
        self.assertEqual(inst.text.div, "<div>[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testContraindication2(self):
        inst = self.instantiate_from("contraindication-example-dup.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2be110> instance")
    
        self.assertEqual(inst.category.coding[0].code, "DUPTHPY")
        self.assertEqual(inst.category.coding[0].display, "Duplicate Therapy Alert")
        self.assertEqual(inst.category.coding[0].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.date.date, FHIRDate("2013-05-08").date)
        self.assertEqual(inst.date.isostring, "2013-05-08")
        self.assertEqual(inst.detail, "Similar test was performed within the past 14 days")
        self.assertEqual(inst.id, "duplicate")
        self.assertEqual(inst.text.status, "generated")
    
    def testContraindication3(self):
        inst = self.instantiate_from("contraindication-example-lab.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2be110> instance")
    
        self.assertEqual(inst.id, "lab")
        self.assertEqual(inst.text.div, "<div>[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testContraindication4(self):
        inst = self.instantiate_from("contraindication-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2be110> instance")
    
        self.assertEqual(inst.category.coding[0].code, "DRG")
        self.assertEqual(inst.category.coding[0].display, "Drug Interaction Alert")
        self.assertEqual(inst.category.coding[0].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.date.date, FHIRDate("2014-01-05").date)
        self.assertEqual(inst.date.isostring, "2014-01-05")
        self.assertEqual(inst.id, "ddi")
        self.assertEqual(inst.mitigation[0].action.coding[0].code, "30")
        self.assertEqual(inst.mitigation[0].action.coding[0].display, "Stopped Concurrent Therapy")
        self.assertEqual(inst.mitigation[0].action.coding[0].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.mitigation[0].action.text, "Asked patient to discontinue regular use of Tylenol and to consult with clinician if they need to resume to allow appropriate INR monitoring")
        self.assertEqual(inst.mitigation[0].date.date, FHIRDate("2014-01-05").date)
        self.assertEqual(inst.mitigation[0].date.isostring, "2014-01-05")
        self.assertEqual(inst.severity, "H")
        self.assertEqual(inst.text.status, "generated")

