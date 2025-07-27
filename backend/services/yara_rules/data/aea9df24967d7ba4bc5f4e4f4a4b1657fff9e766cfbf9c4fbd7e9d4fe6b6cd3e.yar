rule auto_rule_20250726221401_2155 {
  strings:
    $o0 = "_itoa" wide ascii nocase
    $o1 = "Handler" wide ascii nocase
    $o2 = "dword_46481C" wide ascii nocase
  condition:
    3 of ($o*)
}