<div align="center">
  <h1>Ashar</h1>
  <strong>ashar - free & open source project for text encryption with password protection.</strong>
  <br><br>
</div>

[![Test on Ubuntu latest](https://github.com/yasserbdj96/ashar/actions/workflows/python-app-on-linux.yml/badge.svg)](https://github.com/yasserbdj96/ashar/actions/workflows/python-app-on-linux.yml)
[![Test on Windows latest](https://github.com/yasserbdj96/ashar/actions/workflows/python-app-on-win.yml/badge.svg)](https://github.com/yasserbdj96/ashar/actions/workflows/python-app-on-win.yml)
[![Test on MacOS latest](https://github.com/yasserbdj96/ashar/actions/workflows/python-app-on-mac.yml/badge.svg)](https://github.com/yasserbdj96/ashar/actions/workflows/python-app-on-mac.yml)
[![pypi-setup](https://github.com/yasserbdj96/ashar/actions/workflows/pypi-setup.yml/badge.svg)](https://github.com/yasserbdj96/ashar/actions/workflows/pypi-setup.yml)
[![Deploy static content to Pages](https://github.com/yasserbdj96/ashar/actions/workflows/pages.yml/badge.svg)](https://github.com/yasserbdj96/ashar/actions/workflows/pages.yml)
[![CodeQL](https://github.com/yasserbdj96/ashar/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/yasserbdj96/ashar/actions/workflows/codeql-analysis.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/yasserbdj96/ashar/badge)](https://www.codefactor.io/repository/github/yasserbdj96/ashar)
[![Supported Versions](https://img.shields.io/pypi/pyversions/ashar.svg)](https://pypi.org/project/ashar) 
[![Visitors](https://visitor-badge.laobi.icu/badge?page_id=yasserbdj96.ashar&format=true)](https://github.com/yasserbdj96/ashar)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red)](https://github.com/yasserbdj96/ashar)
[![Stars](https://img.shields.io/github/stars/yasserbdj96/ashar?color=red)](https://github.com/yasserbdj96/ashar)
[![Forks](https://img.shields.io/github/forks/yasserbdj96/ashar?color=red)](https://github.com/yasserbdj96/ashar)
[![Watching](https://img.shields.io/github/watchers/yasserbdj96/ashar?label=Watchers&color=red&style=flat-square)](https://github.com/yasserbdj96/ashar)
![GitHub contributors](https://img.shields.io/github/contributors/yasserbdj96/ashar)
![GitHub closed issues](https://img.shields.io/github/issues-closed/yasserbdj96/ashar)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/yasserbdj96/ashar)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/yasserbdj96/ashar)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/yasserbdj96/ashar)
[![GitHub license](https://img.shields.io/github/license/yasserbdj96/ashar)](https://github.com/yasserbdj96/ashar)
[![Join the chat at https://gitter.im/yasserbdj96/ashar](https://badges.gitter.im/yasserbdj96/ashar.svg)](https://gitter.im/yasserbdj96/ashar?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

<br>
<h2>Python Package Installation:</h2>

```
# install from pypi:
>>> pip install ashar

# local install:
>>> git clone https://github.com/yasserbdj96/ashar.git
>>> cd ashar
>>> sudo python setup.py install

# uninstall:
>>> pip uninstall ashar
```

<br>
<h2>Run without installation:</h2>

```
>>> git clone https://github.com/yasserbdj96/ashar.git
>>> cd ashar
>>> python3 run.py <CONDITION*> <PASSWORD*> <TEXT*>
```

<br>
<h2>Script Usage:</h2>

```python
from ashar import ashar
#For encryption
p1=ashar("<PASSWORD>","<TEXT>").encode()
print(p1)
    
#To decrypt
p2=ashar("<PASSWORD>","<ENCRYPTED_TEXT>").decode()
print(p2)

```

<br>
<h2>Script Examples:</h2>

```python
from ashar import ashar
# Example:1
#For encryption
p1=ashar("123","Example:1").encode()
print(p1)
    
#To decrypt
p2=ashar("123",p1).decode()
print(p2)

```

<br>
<h2>Changelog History:</h2>

<details>
  <summary>Click to See changelog History</summary>

```
## 1.1.7 [30-11-2022][Last Version]
 - Bug fixes & performance improvements.

## 1.1.6
 - Delete pipincluder pakage.
 - Fix Bugs.

## 1.1.5
 - Fix Bugs.

## 1.1.4
 - fix bugs.
 - new build.
 
## 1.1.2
 - fix bugs.
 - new build.
 
## 1.1.1
 - Fix bugs.
 
## 1.1.0
 - Import pakages by pipincluder.
 
## 1.0.6
 - You can encrypt anything now.
 - Fix bugs.
 
## 1.0.0
 - Fix bugs.
 
## 0.5.5
 - Fix bugs.
 
## 0.5.4
 - Static encryption.
 - Fix bugs.
 
## 0.5.3
 - Fix bugs.
 
## 0.5.0
 - First public release.
```

</details>


<br>
<h2>Development By:</h2>

Developer / Author: [yasserbdj96](https://github.com/yasserbdj96)

<br>
<h2>License:</h2>

<p>Copyright © 2008->Present, yasserbdj96 (Boudjada Yasser)
<br>
The content of this repository is bound by the following license:</p>

<details>
  <summary>Click to See Apache-2.0 license</summary>

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/
   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
   1. Definitions.
      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.
      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.
      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.
      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.
      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.
      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.
      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).
      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.
      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."
      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.
   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.
   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.
   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:
      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and
      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and
      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and
      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.
      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.
   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.
   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.
   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.
   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.
   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.
   END OF TERMS AND CONDITIONS
   APPENDIX: How to apply the Apache License to your work.
      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.
   Copyright © 2008->Present, yasserbdj96 (Boudjada Yasser).
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```
</details>

<br>
<h2>Support:</h2>
<p>If you like `ashar` and want to see it improve furthur or want me to create intresting projects , You can buy me a coffee </p>
<div align="center">
    <a href="https://ko-fi.com/yasserbdj96">
        <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="ashar by yasserbdj96">
    </a><br>
    BTC: bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9<br>
</div>

<br><br>

<p align="center">
  <samp>
    <a href="https://yasserbdj96.github.io/">website</a> .
    <a href="https://github.com/yasserbdj96">github</a> .
    <a href="https://gitlab.com/yasserbdj96">gitlab</a> .
    <a href="https://www.linkedin.com/in/yasserbdj96">linkedin</a> .
    <a href="https://twitter.com/yasserbdj96">twitter</a> .
    <a href="https://instagram.com/yasserbdj96">instagram</a> .
    <a href="https://www.facebook.com/yasserbdj96">facebook</a> .
    <a href="https://www.youtube.com/@yasserbdj96">youtube</a> .
    <a href="https://pypi.org/user/yasserbdj96">pypi</a> .
    <a href="https://hub.docker.com/u/yasserbdj96">docker</a> .
    <a href="https://t.me/yasserbdj96">telegram</a> .
    <a href="https://gitter.im/yasserbdj96/yasserbdj96">gitter</a> .
    <a href="mailto:yasser.bdj96@gmail.com">e-mail</a> .
    <a href="https://ko-fi.com/yasserbdj96">sponsor</a>
  </samp>
</p>
<br>