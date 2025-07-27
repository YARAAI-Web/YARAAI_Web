rule auto_rule_20250726200637_7801 {
  strings:
    $o0 = "GetKBCodePage" wide ascii nocase
    $o1 = "FileTimeToDosDateTime" wide ascii nocase
    $o2 = "dwThreadId" wide ascii nocase
    $o3 = "LoadBitmapW" wide ascii nocase
  condition:
    4 of ($o*)
}