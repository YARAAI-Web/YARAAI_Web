rule auto_rule_20250726175900_7780 {
  strings:
    $o0 = "dword_43B81C" wide ascii nocase
    $o1 = "dword_43B82F" wide ascii nocase
    $o2 = "dword_43B423" wide ascii nocase
  condition:
    3 of ($o*)
}