rule auto_rule_20250727042539_8008 {
  strings:
    $o0 = "x7A00001" wide ascii nocase
    $o1 = "dword_40E014" wide ascii nocase
    $o2 = "byte_407B50" wide ascii nocase
    $o3 = "__sbh_alloc_block" wide ascii nocase
  condition:
    4 of ($o*)
}