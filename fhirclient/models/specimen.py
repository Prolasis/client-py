#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Specimen) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import period
import quantity


class Specimen(domainresource.DomainResource):
    """ Sample for analysis.
    """
    
    resource_name = "Specimen"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.accessionIdentifier = None
        """ Identifier assigned by the lab.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.collection = None
        """ Collection details.
        Type `SpecimenCollection` (represented as `dict` in JSON). """
        
        self.container = None
        """ Direct container of specimen (tube/slide, etc).
        List of `SpecimenContainer` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.parent = None
        """ Specimen from which this specimen originated.
        List of `FHIRReference` items referencing `Specimen` (represented as `dict` in JSON). """
        
        self.receivedTime = None
        """ The time when specimen was received for processing.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.subject = None
        """ Where the specimen came from. This may be from the patient(s) or
        from the environment or a device.
        Type `FHIRReference` referencing `Patient, Group, Device, Substance` (represented as `dict` in JSON). """
        
        self.treatment = None
        """ Treatment and processing step details.
        List of `SpecimenTreatment` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Kind of material that forms the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Specimen, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Specimen, self).update_with_json(jsondict)
        if 'accessionIdentifier' in jsondict:
            self.accessionIdentifier = identifier.Identifier.with_json_and_owner(jsondict['accessionIdentifier'], self)
        if 'collection' in jsondict:
            self.collection = SpecimenCollection.with_json_and_owner(jsondict['collection'], self)
        if 'container' in jsondict:
            self.container = SpecimenContainer.with_json_and_owner(jsondict['container'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'parent' in jsondict:
            self.parent = fhirreference.FHIRReference.with_json_and_owner(jsondict['parent'], self)
        if 'receivedTime' in jsondict:
            self.receivedTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['receivedTime'], self)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'treatment' in jsondict:
            self.treatment = SpecimenTreatment.with_json_and_owner(jsondict['treatment'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


class SpecimenCollection(fhirelement.FHIRElement):
    """ Collection details.
    
    Details concerning the specimen collection.
    """
    
    resource_name = "SpecimenCollection"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bodySiteCodeableConcept = None
        """ Anatomical collection site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bodySiteReference = None
        """ Anatomical collection site.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """
        
        self.collectedDateTime = None
        """ Collection time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.collectedPeriod = None
        """ Collection time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.collector = None
        """ Who collected the specimen.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.comment = None
        """ Collector comments.
        List of `str` items. """
        
        self.method = None
        """ Technique used to perform collection.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ The quantity of specimen collected.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(SpecimenCollection, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SpecimenCollection, self).update_with_json(jsondict)
        if 'bodySiteCodeableConcept' in jsondict:
            self.bodySiteCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['bodySiteCodeableConcept'], self)
        if 'bodySiteReference' in jsondict:
            self.bodySiteReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['bodySiteReference'], self)
        if 'collectedDateTime' in jsondict:
            self.collectedDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['collectedDateTime'], self)
        if 'collectedPeriod' in jsondict:
            self.collectedPeriod = period.Period.with_json_and_owner(jsondict['collectedPeriod'], self)
        if 'collector' in jsondict:
            self.collector = fhirreference.FHIRReference.with_json_and_owner(jsondict['collector'], self)
        if 'comment' in jsondict:
            self.comment = jsondict['comment']
        if 'method' in jsondict:
            self.method = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['method'], self)
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)


class SpecimenContainer(fhirelement.FHIRElement):
    """ Direct container of specimen (tube/slide, etc).
    
    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """
    
    resource_name = "SpecimenContainer"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.additiveCodeableConcept = None
        """ Additive associated with container.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.additiveReference = None
        """ Additive associated with container.
        Type `FHIRReference` referencing `Substance` (represented as `dict` in JSON). """
        
        self.capacity = None
        """ Container volume or size.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.description = None
        """ Textual description of the container.
        Type `str`. """
        
        self.identifier = None
        """ Id for the container.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.specimenQuantity = None
        """ Quantity of specimen within container.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.type = None
        """ Kind of container directly associated with specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenContainer, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SpecimenContainer, self).update_with_json(jsondict)
        if 'additiveCodeableConcept' in jsondict:
            self.additiveCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['additiveCodeableConcept'], self)
        if 'additiveReference' in jsondict:
            self.additiveReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['additiveReference'], self)
        if 'capacity' in jsondict:
            self.capacity = quantity.Quantity.with_json_and_owner(jsondict['capacity'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'specimenQuantity' in jsondict:
            self.specimenQuantity = quantity.Quantity.with_json_and_owner(jsondict['specimenQuantity'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


class SpecimenTreatment(fhirelement.FHIRElement):
    """ Treatment and processing step details.
    
    Details concerning treatment and processing steps for the specimen.
    """
    
    resource_name = "SpecimenTreatment"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.additive = None
        """ Material used in the processing step.
        List of `FHIRReference` items referencing `Substance` (represented as `dict` in JSON). """
        
        self.description = None
        """ Textual description of procedure.
        Type `str`. """
        
        self.procedure = None
        """ Indicates the treatment or processing step  applied to the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenTreatment, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SpecimenTreatment, self).update_with_json(jsondict)
        if 'additive' in jsondict:
            self.additive = fhirreference.FHIRReference.with_json_and_owner(jsondict['additive'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'procedure' in jsondict:
            self.procedure = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['procedure'], self)

