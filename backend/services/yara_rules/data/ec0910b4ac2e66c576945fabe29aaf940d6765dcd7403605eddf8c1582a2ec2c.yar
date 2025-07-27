rule auto_rule_20250726170128_2192 {
  strings:
    $o0 = "UnwindUp2_0" wide ascii nocase
    $o1 = "byte_40CD28" wide ascii nocase
    $o2 = "dword_412244" wide ascii nocase
  condition:
    3 of ($o*)
}