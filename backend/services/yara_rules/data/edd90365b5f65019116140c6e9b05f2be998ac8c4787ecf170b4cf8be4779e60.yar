rule auto_rule_20250726155910_8123 {
  strings:
    $o0 = "memcpy_0" wide ascii nocase
    $o1 = "Client" wide ascii nocase
    $o2 = "dword_469BD0" wide ascii nocase
  condition:
    3 of ($o*)
}