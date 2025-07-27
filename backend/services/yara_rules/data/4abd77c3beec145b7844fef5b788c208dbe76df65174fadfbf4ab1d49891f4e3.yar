rule auto_rule_20250727004027_6346 {
  strings:
    $o0 = "dword_46429C" wide ascii nocase
    $o1 = "nFile" wide ascii nocase
    $o2 = "byte_463B00" wide ascii nocase
  condition:
    3 of ($o*)
}