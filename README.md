## c8rpi4-aarch64-builder

### 内容
c8rpi4-aarch64-builder は、CentOS Userland 8 for Raspberry Pi 4 (aarch64) のカスタムディスクイメージを作成するスクリプトです。  
※2020年5月27日現在、Raspberry Pi 用の CentOS Userland 8 公式ディスクイメージは公開されていません。

### 要件
- CentOS Userland 8 (aarch64) が稼働している Raspberry Pi 4 Model B
    - [CentOS - Raspberry PI 4 - CentOS Forums](https://forums.centos.org/viewtopic.php?f=55&t=73495)
    - [開発者によるテスト用ディスクイメージ](https://people.centos.org/pgreco/CentOS-Userland-8-stream-aarch64-RaspberryPI-Minimal-4/)
- 16 GB 以上の microSD
- root権限
- lorax-lmc-novirt、git、epel-release、mock、patch および依存パッケージ

### srpm からのビルドと、ディスクイメージ作成の実行例

#### 準備

```
# yum install git patch lorax-lmc-novirt
# git clone https://github.com/lunatilia/c8rpi4-aarch64-builder
# cd c8rpi4-aarch64-builder
# yum install epel-release
# yum install mock
# mock -r centos-stream-aarch64 --init
```

#### srpm からの centos-release と raspberrypi2 のビルド

- centos-release-\*.el8.src.rpm と raspberrypi2-\*.src.rpm は、ソースから事前に作成

```
# mkdir -p /centos/8/{SRPMS,aarch64}
# mock -r centos-stream-aarch64 rebuild centos-release-8.1-1.1911.0.9.el8.src.rpm
# mv /var/lib/mock/centos-stream-aarch64/result/*.src.rpm /centos/8/SRPMS/
# mv /var/lib/mock/centos-stream-aarch64/result/*.rpm /centos/8/aarch64/
# mock -r centos-stream-aarch64 rebuild raspberrypi2-5.4.42-v8.1.el8.src.rpm
# mv /var/lib/mock/centos-stream-aarch64/result/*.src.rpm /centos/8/SRPMS/
# mv /var/lib/mock/centos-stream-aarch64/result/*.rpm /centos/8/aarch64/
# mock -r centos-stream-aarch64 --clean
# yum install createrepo
# createrepo /centos/8/aarch64/
```

#### ディスクイメージ作成

```
# ./c8rpi4-aarch64-builder kickstarts/c8rpi4-minimal-ks.cfg
```

### ディスクイメージ
- [ディスクイメージのダウンロード](https://github.com/lunatilia/c8rpi4-aarch64-builder/releases/tag/0.1.0-20200527)

### ライセンス
[GNU General Public License v2.0](https://github.com/lunatilia/c8rpi4-aarch64-builder/blob/master/LICENSE) (The CentOS Projectのデフォルトライセンス)

### 参考

#### centos-release および raspberrypi2 のソース

- [rpms / centos-release - git.centos.org](https://git.centos.org/rpms/centos-release)
- [rpms / raspberrypi2 - git.centos.org](https://git.centos.org/rpms/raspberrypi2)
