rule auto_rule_20250726172856_1930 {
  strings:
    $o0 = "dword_433EE4" wide ascii nocase
    $o1 = "SHBrowseForFolderW" wide ascii nocase
  condition:
    all of them
}