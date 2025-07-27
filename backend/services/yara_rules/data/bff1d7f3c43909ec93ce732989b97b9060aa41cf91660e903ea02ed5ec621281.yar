rule auto_rule_20250726203211_5071 {
  strings:
    $o0 = "CharUpperA" wide ascii nocase
    $o1 = "DlgDirListComboBoxA" wide ascii nocase
  condition:
    all of them
}