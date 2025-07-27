rule auto_rule_20250726230916_9547 {
  strings:
    $o0 = "byte_40639C" wide ascii nocase
    $o1 = "aJpgImageFilesJ" wide ascii nocase
    $o2 = "dword_406370" wide ascii nocase
  condition:
    3 of ($o*)
}