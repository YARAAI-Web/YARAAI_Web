rule auto_rule_20250726183640_5073 {
  strings:
    $o0 = "__vcrt_uninitialize_ptd" wide ascii nocase
    $o1 = "dword_4148EC" wide ascii nocase
  condition:
    all of them
}