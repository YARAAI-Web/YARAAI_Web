rule auto_rule_20250727033726_2598 {
  strings:
    $o0 = "universal" wide ascii nocase
    $o1 = "dword_414AF4" wide ascii nocase
    $o2 = "_JumpToContinuation" wide ascii nocase
  condition:
    3 of ($o*)
}