rule auto_rule_20250726140027_5869 {
  strings:
    $o0 = "LoadBitmapW" wide ascii nocase
    $o1 = "SetWaitableTimer" wide ascii nocase
    $o2 = "dwPartition" wide ascii nocase
  condition:
    3 of ($o*)
}