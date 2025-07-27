rule auto_rule_20250726212958_9850 {
  strings:
    $o0 = "lpNumberOfCharsRead" wide ascii nocase
    $o1 = "lpSystemPowerStatus" wide ascii nocase
    $o2 = "GetCurrentConsoleFont" wide ascii nocase
    $o3 = "ucchMax" wide ascii nocase
  condition:
    4 of ($o*)
}