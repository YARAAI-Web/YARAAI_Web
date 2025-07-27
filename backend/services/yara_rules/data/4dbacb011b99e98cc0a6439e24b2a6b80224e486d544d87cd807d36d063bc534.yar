rule auto_rule_20250726110448_5121 {
  strings:
    $o0 = "DlgDirListW" wide ascii nocase
    $o1 = "lpStruct" wide ascii nocase
    $o2 = "SetCalendarInfoA" wide ascii nocase
    $o3 = "lpArgToCompletionRoutine" wide ascii nocase
  condition:
    4 of ($o*)
}