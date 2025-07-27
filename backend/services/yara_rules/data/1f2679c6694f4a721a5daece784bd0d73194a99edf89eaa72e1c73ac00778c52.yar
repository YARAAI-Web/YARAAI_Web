rule auto_rule_20250726171327_4067 {
  strings:
    $o0 = "lpszFormatName" wide ascii nocase
    $o1 = "keybd_event" wide ascii nocase
  condition:
    all of them
}