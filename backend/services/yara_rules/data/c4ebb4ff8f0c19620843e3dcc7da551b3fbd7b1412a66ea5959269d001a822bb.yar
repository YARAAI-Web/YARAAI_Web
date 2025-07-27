rule auto_rule_20250726203537_9255 {
  strings:
    $o0 = "x3FFFFFF" wide ascii nocase
    $o1 = "dwCreationFlags" wide ascii nocase
    $o2 = "dword_46D014" wide ascii nocase
    $o3 = "byte_46D778" wide ascii nocase
  condition:
    4 of ($o*)
}