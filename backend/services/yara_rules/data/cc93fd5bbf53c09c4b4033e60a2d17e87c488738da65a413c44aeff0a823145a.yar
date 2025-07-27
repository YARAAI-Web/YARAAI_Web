rule auto_rule_20250726162147_3342 {
  strings:
    $o0 = "aProgid" wide ascii nocase
    $o1 = "dword_4173D4" wide ascii nocase
  condition:
    all of them
}