rule auto_rule_20250726233133_9748 {
  strings:
    $o0 = "GetProfileStringW" wide ascii nocase
    $o1 = "nIDCheckButton" wide ascii nocase
    $o2 = "dword_401A38" wide ascii nocase
    $o3 = "lstrlenW" wide ascii nocase
    $o4 = "SetPixel" wide ascii nocase
  condition:
    4 of ($o*)
}