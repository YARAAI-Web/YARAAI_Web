rule auto_rule_20250726122019_1314 {
  strings:
    $o0 = "dword_46428C" wide ascii nocase
    $o1 = "_itoa" wide ascii nocase
  condition:
    all of them
}