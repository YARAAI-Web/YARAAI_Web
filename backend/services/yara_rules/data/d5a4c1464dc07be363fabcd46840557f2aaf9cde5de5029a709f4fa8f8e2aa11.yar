rule auto_rule_20250726094905_9819 {
  strings:
    $o0 = "dwExceptionFlags" wide ascii nocase
    $o1 = "x404893" wide ascii nocase
    $o2 = "dwCreationDisposition" wide ascii nocase
  condition:
    3 of ($o*)
}