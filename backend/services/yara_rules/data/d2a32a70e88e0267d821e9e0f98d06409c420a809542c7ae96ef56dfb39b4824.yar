rule auto_rule_20250727022306_4398 {
  strings:
    $o0 = "dword_7C6F94" wide ascii nocase
    $o1 = "xADE0021" wide ascii nocase
    $o2 = "byte_791318" wide ascii nocase
  condition:
    3 of ($o*)
}