rule auto_rule_20250727041448_9637 {
  strings:
    $o0 = "cbOff" wide ascii nocase
    $o1 = "lpPoints" wide ascii nocase
    $o2 = "hAccelSrc" wide ascii nocase
    $o3 = "lpChar" wide ascii nocase
  condition:
    4 of ($o*)
}