rule auto_rule_20250726055746_1824 {
  strings:
    $o0 = "main_loop_1" wide ascii nocase
    $o1 = "differ" wide ascii nocase
    $o2 = "x402B85" wide ascii nocase
    $o3 = "CreateSemaphoreA" wide ascii nocase
    $o4 = "dword_41D028" wide ascii nocase
  condition:
    4 of ($o*)
}