rule auto_rule_20250726085520_3696 {
  strings:
    $o0 = "cause" wide ascii nocase
    $o1 = "dword_46EF84" wide ascii nocase
    $o2 = "finish_loop" wide ascii nocase
    $o3 = "pavi" wide ascii nocase
    $o4 = "__crtExitProcess" wide ascii nocase
  condition:
    4 of ($o*)
}