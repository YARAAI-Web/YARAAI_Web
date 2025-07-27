rule auto_rule_20250726181403_9303 {
  strings:
    $o0 = "lpNumberOfCharsWritten" wide ascii nocase
    $o1 = "hNamedPipe" wide ascii nocase
    $o2 = "SetConsoleTitleW" wide ascii nocase
  condition:
    3 of ($o*)
}