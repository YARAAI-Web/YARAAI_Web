rule auto_rule_20250726234705_5759 {
  strings:
    $o0 = "dword_40CA10" wide ascii nocase
    $o1 = "_cropzeros" wide ascii nocase
  condition:
    all of them
}