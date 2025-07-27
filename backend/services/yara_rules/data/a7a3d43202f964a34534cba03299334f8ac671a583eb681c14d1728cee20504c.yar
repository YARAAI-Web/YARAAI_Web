rule auto_rule_20250727022055_2560 {
  strings:
    $o0 = "x2320" wide ascii nocase
    $o1 = "dword_42C014" wide ascii nocase
    $o2 = "x6981u" wide ascii nocase
  condition:
    3 of ($o*)
}