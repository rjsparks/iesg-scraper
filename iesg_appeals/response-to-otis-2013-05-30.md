 
IESG Report regarding "Appeal of decision to advance RFC6376"


June 27, 2013


### Summary:


Douglas Otis and Dave Rand have appealed the action taken by the IESG to 
 advance RFC 6376, DomainKeys Identified Mail (DKIM) Signatures, from 
 (the legacy status of) Draft Standard to Internet Standard. The document 
 was advanced under the criteria defined in section 2 of RFC 6410. The 
 IESG has taken this to be an appeal under section 6.5.2 of RFC 2026. 
 Following the procedure described there, the IESG has reviewed the 
 complaint and re-examined the advancement of RFC 6376 to Internet 
 Standard. We have concluded that the criteria for advancement to 
 Internet Standard have been met and that our action was correct. No 
 further action is warranted.


### Background:


This appeal appears to be brought under section 6.5.2 of RFC 2026:



> 
> If an individual should disagree with an action taken by the IESG in  
> 
>  this process, that person should first discuss the issue with the  
> 
>  IESG Chair. If the IESG Chair is unable to satisfy the complainant  
> 
>  then the IESG as a whole should re-examine the action taken, along  
> 
>  with input from the complainant, and determine whether any further  
> 
>  action is needed. The IESG shall issue a report on its review of the  
> 
>  complaint to the IETF.
> 
> 
> 


Normally, an appeal on the basis of a technical error would be brought 
 under section 6.5.1 of RFC 2026, claiming "the Working Group has made an 
 incorrect technical choice which places the quality and/or integrity of 
 the Working Group's product(s) in significant jeopardy." However, the 
 time for that sort of appeal (within two months of the action) is long 
 past, since the Working Group in question has since closed. Nonetheless, 
 the appeal sets forth new technical information and complains that 
 advancement to Internet Standard is unwarranted. That is a valid basis 
 for an appeal of advancement as an IESG action under section 6.5.2.  

  

 After reviewing the criteria for advancement to Internet Standard 
 defined in section 2 of RFC 6410, we have concluded that this appeal is 
 claiming that criteria (1) has not been satisified:



> 
> (1) There are at least two independent interoperating implementations
>  with widespread deployment and successful operational experience.
> 
> 
> 


In particular, since this appeal is based on a purported technical error 
 in the spec, we read the appeal to mean that interoperability and "successful operational experience" have not been appropriately 
 established. None of the other criteria appear to make sense in the 
 context of this appeal.


RFC 6376 is currently at the abandoned status of Draft Standard, which 
 it obtained when advancing RFC 4871 from Proposed Standard. This 
 occurred prior to the publication of RFC 6410, hence the use of the old 
 Draft Standard status.



> 
> <http://datatracker.ietf.org/doc/draft-ietf-dkim-rfc4871bis/>
> 
> 
> 


An interoperability report was prepared at that time:



> 
> <http://www.ietf.org/iesg/implementation/report-rfc4871.txt>
> 
> 
> 


In evaluating this appeal, we therefore tried to determine if anything 
 of the new information provided indicates that the interoperability and 
 successful operational experience has changed since issuance of that 
 report, in particular the issues raised in the cited Internet-Draft 
 prepared prior to and during this appeal:



> 
> <https://datatracker.ietf.org/doc/draft-otis-dkim-harmful/>
> 
> 
> 


We have also reviewed the messages posted to the IETF discussion list 
 responding to draft-otis-dkim-harmful.


### Analysis:


The argument set forth in draft-otis-dkim-harmful is that there is a way 
 to construct or alter an email message that will have a DKIM signature 
 that validates as per RFC 6376, have a second "From:" header field 
 prepended to it (rendering the message non-conforming to RFC 5322) that 
 will not be in the scope of data signed in the DKIM signature, and 
 therefore be accepted through a spam filter and presented to the 
 end-user as being both DKIM-validated and appearing to be "from" the 
 address in the prepended "From:" field that was not included in the DKIM 
 signature. The draft concludes that therefore the DKIM specification 
 needs to require that messages with multiple "From:" header fields be 
 rejected as part of the protocol itself.  

  

 However, as described in the recent discussion on the main IETF mailing 
 list, the DKIM Working Group considered this argument during document 
 development and concluded the following:  

  

 - DKIM itself is designed to allow the sending MTA to attach a 
 signature-authenticated domain name to an email message such that the 
 receiver can validate that signature. In particular, DKIM is not a 
 complete anti-spam solution and it is not a solution to secure the 
 entire content of a message from in-transit modification. A valid DKIM 
 signature cannot, in and of itself, identify a message as not having 
 been altered, and it cannot identify a message as not being spam. 
 Therefore, the addition of a requirement to identify all such 
 alterations was considered out of scope for the protocol.  

  

 - Other parts of a spam system are perfectly well able to identify a 
 message with multiple "From:" header fields as suspicious and therefore 
 mark the message as improperly modified or as spam. A change to the DKIM 
 spec to handle this case was seen as unnecessary.  

  

 - The document does give advice on how to avoid the potential for 
 problems. It describes the possibility of inserting an extra "From:" field, the limitations of what information DKIM actually provides, and 
 what can be done in the context of DKIM if a sending MTA does want to 
 not have the signature validate in such a case.  

  

 The conclusion of the WG was that the concern was considered, but that 
 the risk associated with extra "From:" fields was sufficiently mitigated 
 by the text in the document and that the opinion expressed in 
 draft-otis-dkim-harmful was an outlier.  

  

 The appeal argues that the above conclusions are not satisfactory, and 
 that new information makes it appropriate to revisit the conclusion and 
 therefore not reclassify the document as Internet Standard. The Internet 
 Draft states that the appellants' tests indicate that there are a 
 significant increase in the number of messages with valid DKIM 
 signatures that have multiple "From:" fields. However, other posters to 
 the IETF list indicate that they are seeing no such significant 
 appearance of messages with valid DKIM signatures and multiple "From:" fields. Furthermore, even if such messages did appear, the appellants 
 provide no data to indicate that spam engines are accepting these 
 messages solely based on the DKIM signature, and they provide no data to 
 indicate that such messages are being displayed to end users 
 inappropriately as "certified not spam" with the additional "From:" field being displayed as the author of the message.  

  

 Therefore, we find nothing in the appeal to indicate that DKIM itself is 
 non-interoperable or that its deployment has not been successful. We 
 conclude that the decision to move the document to Internet Standard was 
 appropriate. No change of action will be made.


 