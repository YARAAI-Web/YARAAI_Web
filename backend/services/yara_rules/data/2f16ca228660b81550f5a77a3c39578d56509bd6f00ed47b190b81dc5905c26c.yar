rule auto_rule_20250727033225_7715 {
  strings:
    $o0 = "x6B70" wide ascii nocase
    $o1 = "aUtzTa9308oc5" wide ascii nocase
    $o2 = "x4F8A" wide ascii nocase
  condition:
    3 of ($o*)
}