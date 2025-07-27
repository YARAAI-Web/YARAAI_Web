rule auto_rule_20250726081131_7216 {
  strings:
    $o0 = "__m128" wide ascii nocase
    $o1 = "MmUnmapIoSpace" wide ascii nocase
    $o2 = "dword_140005300" wide ascii nocase
  condition:
    3 of ($o*)
}