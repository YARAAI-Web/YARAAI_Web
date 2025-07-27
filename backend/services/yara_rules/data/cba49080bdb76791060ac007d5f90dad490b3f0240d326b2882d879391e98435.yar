rule auto_rule_20250726211827_9362 {
  strings:
    $o0 = "dword_460614" wide ascii nocase
    $o1 = "UnwindUp2_0" wide ascii nocase
  condition:
    all of them
}