rule auto_rule_20250726112735_2353 {
  strings:
    $o0 = "uIDEnableItem" wide ascii nocase
    $o1 = "WriteProcessMemory" wide ascii nocase
    $o2 = "WaitNamedPipeW" wide ascii nocase
    $o3 = "dwInitParam" wide ascii nocase
  condition:
    4 of ($o*)
}