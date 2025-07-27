rule auto_rule_20250726194259_3863 {
  strings:
    $o0 = "GetAtomNameW" wide ascii nocase
    $o1 = "AreFileApisANSI" wide ascii nocase
    $o2 = "off_42E53B" wide ascii nocase
  condition:
    3 of ($o*)
}