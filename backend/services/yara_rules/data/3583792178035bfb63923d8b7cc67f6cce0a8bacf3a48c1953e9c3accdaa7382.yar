rule auto_rule_20250726112938_2616 {
  strings:
    $o0 = "ImageList_LoadImageA" wide ascii nocase
    $o1 = "GetCompressedFileSizeA" wide ascii nocase
    $o2 = "SetThreadPriority" wide ascii nocase
  condition:
    3 of ($o*)
}