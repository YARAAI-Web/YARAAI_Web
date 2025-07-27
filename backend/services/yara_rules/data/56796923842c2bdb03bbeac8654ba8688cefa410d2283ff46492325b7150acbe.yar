rule auto_rule_20250726172319_2793 {
  strings:
    $o0 = "dword_6403147C" wide ascii nocase
    $o1 = "byte_64027702" wide ascii nocase
  condition:
    all of them
}