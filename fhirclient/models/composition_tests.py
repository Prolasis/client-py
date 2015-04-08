#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import composition
from fhirdate import FHIRDate


class CompositionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = composition.Composition(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testComposition1(self):
        inst = self.instantiate_from("composition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e293550> instance")
    
        self.assertEqual(inst.attester[0].mode[0], "legal")
        self.assertEqual(inst.confidentiality, "N")
        self.assertEqual(inst.date.date, FHIRDate("2012-01-04T09:10:14Z").date)
        self.assertEqual(inst.date.isostring, "2012-01-04T09:10:14Z")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://healthintersections.com.au/test")
        self.assertEqual(inst.identifier.value, "1")
        self.assertEqual(inst.section[0].title, "History of present illness")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.div, "<div>\n      \n      <p>Consultation note for Henry Levin the 7th</p>\n    \n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "11488-4")
        self.assertEqual(inst.type.coding[0].display, "Consult note")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")

