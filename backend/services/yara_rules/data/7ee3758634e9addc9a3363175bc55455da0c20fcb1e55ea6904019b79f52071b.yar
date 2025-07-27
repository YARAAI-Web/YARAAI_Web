rule auto_rule_20250726155840_9632 {
  strings:
    $o0 = "dword_42A008" wide ascii nocase
    $o1 = "szCSDVersion" wide ascii nocase
    $o2 = "x41C4u" wide ascii nocase
  condition:
    3 of ($o*)
}