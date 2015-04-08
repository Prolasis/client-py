#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import procedure
from fhirdate import FHIRDate


class ProcedureTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = procedure.Procedure(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testProcedure1(self):
        inst = self.instantiate_from("procedure-example-biopsy.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e371b50> instance")
    
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].code, "368225008")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].display, "Entire Left Forearm")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.text, "Left forearm")
        self.assertEqual(inst.followUp[0].text, "Review in clinic")
        self.assertEqual(inst.id, "biopsy")
        self.assertEqual(inst.indication[0].text, "Dark lesion l) forearm. getting darker last 3 months.")
        self.assertEqual(inst.notes, "Standard Biopsy")
        self.assertEqual(inst.performedDateTime.date, FHIRDate("2014-02-03").date)
        self.assertEqual(inst.performedDateTime.isostring, "2014-02-03")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div>Biopsy of suspected melanoma L) arm</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "90105005")
        self.assertEqual(inst.type.coding[0].display, "Biopsy of soft tissue of forearm (Procedure)")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type.text, "Biopsy of suspected melanoma L) arm")
    
    def testProcedure2(self):
        inst = self.instantiate_from("procedure-example-f001-heart.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e371b50> instance")
    
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].code, "17401000")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].display, "Heart valve structure")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.followUp[0].text, "described in care plan")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.indication[0].text, "Heart valve disorder")
        self.assertEqual(inst.outcome.text, "improved blood circulation")
        self.assertEqual(inst.performedPeriod.end.date, FHIRDate("2011-06-27").date)
        self.assertEqual(inst.performedPeriod.end.isostring, "2011-06-27")
        self.assertEqual(inst.performedPeriod.start.date, FHIRDate("2011-06-26").date)
        self.assertEqual(inst.performedPeriod.start.isostring, "2011-06-26")
        self.assertEqual(inst.performer[0].role.coding[0].code, "01.000")
        self.assertEqual(inst.performer[0].role.coding[0].display, "Arts")
        self.assertEqual(inst.performer[0].role.coding[0].system, "urn:oid:2.16.840.1.113883.2.4.15.111")
        self.assertEqual(inst.performer[0].role.text, "Care role")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "34068001")
        self.assertEqual(inst.type.coding[0].display, "Heart valve replacement")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testProcedure3(self):
        inst = self.instantiate_from("procedure-example-f002-lung.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e371b50> instance")
    
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].code, "39607008")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].display, "Lung structure")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.followUp[0].text, "described in care plan")
        self.assertEqual(inst.id, "f002")
        self.assertEqual(inst.indication[0].text, "Malignant tumor of lung")
        self.assertEqual(inst.outcome.text, "improved blood circulation")
        self.assertEqual(inst.performedPeriod.end.date, FHIRDate("2013-03-08T09:30:10+01:00").date)
        self.assertEqual(inst.performedPeriod.end.isostring, "2013-03-08T09:30:10+01:00")
        self.assertEqual(inst.performedPeriod.start.date, FHIRDate("2013-03-08T09:00:10+01:00").date)
        self.assertEqual(inst.performedPeriod.start.isostring, "2013-03-08T09:00:10+01:00")
        self.assertEqual(inst.performer[0].role.coding[0].code, "01.000")
        self.assertEqual(inst.performer[0].role.coding[0].display, "Arts")
        self.assertEqual(inst.performer[0].role.coding[0].system, "urn:oid:2.16.840.1.113883.2.4.15.111")
        self.assertEqual(inst.performer[0].role.text, "Care role")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "359615001")
        self.assertEqual(inst.type.coding[0].display, "Partial lobectomy of lung")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testProcedure4(self):
        inst = self.instantiate_from("procedure-example-f003-abscess.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e371b50> instance")
    
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].code, "83030008")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].display, "Retropharyngeal area")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.followUp[0].text, "described in care plan")
        self.assertEqual(inst.id, "f003")
        self.assertEqual(inst.indication[0].text, "abcess in retropharyngeal area")
        self.assertEqual(inst.outcome.text, "removal of the retropharyngeal abscess")
        self.assertEqual(inst.performedPeriod.end.date, FHIRDate("2013-03-24T10:30:10+01:00").date)
        self.assertEqual(inst.performedPeriod.end.isostring, "2013-03-24T10:30:10+01:00")
        self.assertEqual(inst.performedPeriod.start.date, FHIRDate("2013-03-24T09:30:10+01:00").date)
        self.assertEqual(inst.performedPeriod.start.isostring, "2013-03-24T09:30:10+01:00")
        self.assertEqual(inst.performer[0].role.coding[0].code, "01.000")
        self.assertEqual(inst.performer[0].role.coding[0].display, "Arts")
        self.assertEqual(inst.performer[0].role.coding[0].system, "urn:oid:2.16.840.1.113883.2.4.15.111")
        self.assertEqual(inst.performer[0].role.text, "Care role")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "172960003")
        self.assertEqual(inst.type.coding[0].display, "Incision of retropharyngeal abscess")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testProcedure5(self):
        inst = self.instantiate_from("procedure-example-f004-tracheotomy.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e371b50> instance")
    
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].code, "83030008")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].display, "Retropharyngeal area")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.followUp[0].text, "described in care plan")
        self.assertEqual(inst.id, "f004")
        self.assertEqual(inst.indication[0].text, "ensure breathing during surgery")
        self.assertEqual(inst.outcome.text, "removal of the retropharyngeal abscess")
        self.assertEqual(inst.performedPeriod.end.date, FHIRDate("2013-03-22T10:30:10+01:00").date)
        self.assertEqual(inst.performedPeriod.end.isostring, "2013-03-22T10:30:10+01:00")
        self.assertEqual(inst.performedPeriod.start.date, FHIRDate("2013-03-22T09:30:10+01:00").date)
        self.assertEqual(inst.performedPeriod.start.isostring, "2013-03-22T09:30:10+01:00")
        self.assertEqual(inst.performer[0].role.coding[0].code, "01.000")
        self.assertEqual(inst.performer[0].role.coding[0].display, "Arts")
        self.assertEqual(inst.performer[0].role.coding[0].system, "urn:oid:2.16.840.1.113883.2.4.15.111")
        self.assertEqual(inst.performer[0].role.text, "Care role")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "48387007")
        self.assertEqual(inst.type.coding[0].display, "Tracheotomy")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testProcedure6(self):
        inst = self.instantiate_from("procedure-example-f201-tpf.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e371b50> instance")
    
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].code, "272676008")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].display, "Sphenoid bone")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.indication[0].text, "DiagnosticReport/f201")
        self.assertEqual(inst.notes, "Eerste neo-adjuvante TPF-kuur bij groot proces in sphenoid met intracraniale uitbreiding.")
        self.assertEqual(inst.performedPeriod.end.date, FHIRDate("2013-01-28T14:27:00+01:00").date)
        self.assertEqual(inst.performedPeriod.end.isostring, "2013-01-28T14:27:00+01:00")
        self.assertEqual(inst.performedPeriod.start.date, FHIRDate("2013-01-28T13:31:00+01:00").date)
        self.assertEqual(inst.performedPeriod.start.isostring, "2013-01-28T13:31:00+01:00")
        self.assertEqual(inst.performer[0].role.coding[0].code, "310512001")
        self.assertEqual(inst.performer[0].role.coding[0].display, "Medical oncologist")
        self.assertEqual(inst.performer[0].role.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "367336001")
        self.assertEqual(inst.type.coding[0].display, "Chemotherapy")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testProcedure7(self):
        inst = self.instantiate_from("procedure-example-implant.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e371b50> instance")
    
        self.assertEqual(inst.device[0].action.coding[0].code, "implanted")
        self.assertEqual(inst.device[0].action.coding[0].system, "http://hl7.org/fhir/device-action")
        self.assertEqual(inst.followUp[0].text, "ROS 5 days  - 2013-04-10")
        self.assertEqual(inst.id, "example-implant")
        self.assertEqual(inst.indication[0].text, "Bradycardia")
        self.assertEqual(inst.notes, "Routine Appendectomy. Appendix was inflamed and in retro-caecal position")
        self.assertEqual(inst.performedDateTime.date, FHIRDate("2015-04-05").date)
        self.assertEqual(inst.performedDateTime.isostring, "2015-04-05")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "25267002")
        self.assertEqual(inst.type.coding[0].display, "Insertion of intracardiac pacemaker (procedure)")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type.text, "Implant Pacemaker")
    
    def testProcedure8(self):
        inst = self.instantiate_from("procedure-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e371b50> instance")
    
        self.assertEqual(inst.followUp[0].text, "ROS 5 days  - 2013-04-10")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.indication[0].text, "Generalized abdominal pain 24 hours. Localized in RIF with rebound and guarding")
        self.assertEqual(inst.notes, "Routine Appendectomy. Appendix was inflamed and in retro-caecal position")
        self.assertEqual(inst.performedDateTime.date, FHIRDate("2013-04-05").date)
        self.assertEqual(inst.performedDateTime.isostring, "2013-04-05")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div>Routine Appendectomy</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "80146002")
        self.assertEqual(inst.type.coding[0].display, "Appendectomy (Procedure)")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type.text, "Appendectomy")
    
    def testProcedure9(self):
        inst = self.instantiate_from("procedure-qicore-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e371b50> instance")
    
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].code, "66754008")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].display, "Appendix structure")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/procedure-approachBodySite")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/procedure-incisionDateTime")
        self.assertEqual(inst.extension[1].valueDateTime.date, FHIRDate("2013-04-05T09:30:00-04:00").date)
        self.assertEqual(inst.extension[1].valueDateTime.isostring, "2013-04-05T09:30:00-04:00")
        self.assertEqual(inst.id, "qicore")
        self.assertEqual(inst.indication[0].coding[0].code, "163220003")
        self.assertEqual(inst.indication[0].coding[0].display, "On examination - abdominal pain - right iliac")
        self.assertEqual(inst.indication[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.performedPeriod.end.date, FHIRDate("2013-04-05T10:30:00-04:00").date)
        self.assertEqual(inst.performedPeriod.end.isostring, "2013-04-05T10:30:00-04:00")
        self.assertEqual(inst.performedPeriod.start.date, FHIRDate("2013-04-05T09:20:00-04:00").date)
        self.assertEqual(inst.performedPeriod.start.isostring, "2013-04-05T09:20:00-04:00")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "80146002")
        self.assertEqual(inst.type.coding[0].display, "Appendectomy (Procedure)")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type.text, "Appendectomy")

