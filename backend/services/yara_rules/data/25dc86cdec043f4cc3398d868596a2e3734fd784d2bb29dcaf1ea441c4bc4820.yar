rule auto_rule_20250726194909_6757 {
  strings:
    $o0 = "_global_unwind2" wide ascii nocase
    $o1 = "dword_445C70" wide ascii nocase
  condition:
    all of them
}