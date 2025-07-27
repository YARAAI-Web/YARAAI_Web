rule auto_rule_20250726153832_0813 {
  strings:
    $o0 = "aClassesClsid00" wide ascii nocase
    $o1 = "OpenEventW" wide ascii nocase
    $o2 = "pcbDataSize" wide ascii nocase
    $o3 = "cchFileNameMax" wide ascii nocase
  condition:
    4 of ($o*)
}