rule auto_rule_20250726091715_5567 {
  strings:
    $o0 = "dword_46D55C" wide ascii nocase
    $o1 = "_cftof" wide ascii nocase
  condition:
    all of them
}