rule auto_rule_20250726083828_6798 {
  strings:
    $o0 = "istream" wide ascii nocase
    $o1 = "AfxFindResourceHandle" wide ascii nocase
    $o2 = "OpenDocumentFile" wide ascii nocase
    $o3 = "off_4066D0" wide ascii nocase
    $o4 = "bound" wide ascii nocase
  condition:
    5 of ($o*)
}