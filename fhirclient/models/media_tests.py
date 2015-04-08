#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import media
from fhirdate import FHIRDate


class MediaTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = media.Media(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testMedia1(self):
        inst = self.instantiate_from("media-example-dicom.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e31f490> instance")
    
        self.assertEqual(inst.content.contentType, "application/dicom")
        self.assertEqual(inst.deviceName, "G.E. Medical Systems")
        self.assertEqual(inst.extension[0].url, "http://nema.org/fhir/extensions#0002-0010")
        self.assertEqual(inst.extension[0].valueUri, "urn:oid:1.2.840.10008.1.2.1")
        self.assertEqual(inst.height, 480)
        self.assertEqual(inst.id, "1.2.840.11361907579238403408700.3.0.14.19970327150033")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].type.text, "InstanceUID")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "urn:oid:1.2.840.11361907579238403408700.3.0.14.19970327150033")
        self.assertEqual(inst.identifier[1].system, "http://acme-imaging.com/accession/2012")
        self.assertEqual(inst.identifier[1].type.text, "accessionNo")
        self.assertEqual(inst.identifier[1].value, "1234567")
        self.assertEqual(inst.identifier[2].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[2].type.text, "studyId")
        self.assertEqual(inst.identifier[2].value, "urn:oid:1.2.840.113619.2.21.848.34082.0.538976288.3")
        self.assertEqual(inst.identifier[3].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[3].type.text, "seriesId")
        self.assertEqual(inst.identifier[3].value, "urn:oid:1.2.840.113619.2.21.3408.700.0.757923840.3.0")
        self.assertEqual(inst.subtype.coding[0].code, "US")
        self.assertEqual(inst.subtype.coding[0].system, "http://nema.org/dicom/dicm")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "photo")
        self.assertEqual(inst.width, 640)
    
    def testMedia2(self):
        inst = self.instantiate_from("media-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e31f490> instance")
    
        self.assertEqual(inst.content.contentType, "image/gif")
        self.assertEqual(inst.content.creation.date, FHIRDate("2009-09-03").date)
        self.assertEqual(inst.content.creation.isostring, "2009-09-03")
        self.assertEqual(inst.content.id, "a1")
        self.assertEqual(inst.deviceName, "Acme Camera")
        self.assertEqual(inst.height, 145)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.subtype.coding[0].code, "diagram")
        self.assertEqual(inst.subtype.coding[0].system, "http://hl7.org/fhir/media-method")
        self.assertEqual(inst.text.div, "<div>Diagram for Patient Henry Levin (MRN 12345):\n      <br/>\n      <img alt=\"diagram\" src=\"#11\"/>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "photo")
        self.assertEqual(inst.width, 126)

