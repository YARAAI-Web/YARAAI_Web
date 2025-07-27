rule auto_rule_20250727002558_9342 {
  strings:
    $o0 = "TargetBufferLength" wide ascii nocase
    $o1 = "lpNewItem" wide ascii nocase
    $o2 = "GetThreadSelectorEntry" wide ascii nocase
    $o3 = "IMPQueryIMEW" wide ascii nocase
  condition:
    4 of ($o*)
}